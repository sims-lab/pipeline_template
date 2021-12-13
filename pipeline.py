"""
===========================
Pipeline template
===========================

.. Replace the documentation below with your own description of the
   pipeline's purpose

Overview
========

This pipeline computes the word frequencies in the configuration
files :file:``config.yml` and :file:`conf.py`.

Usage
=====

See :ref:`PipelineSettingUp` and :ref:`PipelineRunning` on general
information how to use cgat pipelines.

Configuration
-------------

The pipeline requires a configured :file:`pipeline.yml` file.
cgatReport report requires a :file:`conf.py` and optionally a
:file:`cgatreport.yml` file (see :ref:`PipelineReporting`).

Default configuration files can be generated by executing:

   python <srcdir>/pipeline_@template@.py config

Input files
-----------

None required except the pipeline configuration files.

Requirements
------------

The pipeline requires the results from
:doc:`pipeline_annotations`. Set the configuration variable
:py:data:`annotations_database` and :py:data:`annotations_dir`.

Pipeline output
===============

.. Describe output files of the pipeline here

Glossary
========

.. glossary::


Code
====

"""

###########
# Imports #
###########

from ruffus import *
import sys
import os
import cgatcore.experiment as E
from cgatcore import pipeline as P

#################
# Configuration #
#################

# Load parameters from config file, located in `./config/pipeline.yml`.
PARAMS = P.get_parameters(
    "%s/config/pipeline.yml" % os.path.dirname(os.path.realpath(__file__))
)

############
# Workflow #
############


@follows(mkdir("results"))
@transform("config/pipeline.yml", regex("config/(.*)"), r"results/\1.counts")
def countWords(infile, outfile):
    """
    Count the number of words in the pipeline configuration file.
    """

    # Declare the command line statement we want to execute
    statement = """
        awk '
            BEGIN { printf("word\\tfreq\\n"); }
            { for (i = 1; i <= NF; i++) freq[$i]++ }
            END { for (word in freq) printf "%%s\\t%%d\\n", word, freq[word] }
            '
        < %(infile)s > %(outfile)s
        """

    # Execute the statement.
    #
    # The statement is interpolated with any options that are defined
    # in the configuration files or variable that are declared in the calling function.
    # For example, %(infile)s will we substituted with the contents of the variable `infile`.
    P.run(statement, job_condaenv="pipeline_template")


@transform(countWords, suffix(".counts"), "_counts.load")
def loadWordCounts(infile, outfile):
    """
    Load results of word counting into database.
    """
    P.load(infile, outfile, "--add-index=word")


@follows(loadWordCounts)
def full():
    pass


##################
# Main execution #
##################


def main(argv=None):
    if argv is None:
        argv = sys.argv
    P.main(argv)


if __name__ == "__main__":
    sys.exit(P.main(sys.argv))
