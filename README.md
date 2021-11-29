[![CI](https://github.com/sims-lab/pipeline_template/actions/workflows/build.yml/badge.svg)](https://github.com/sims-lab/pipeline_template/actions/workflows/build.yml)

# pipeline_template

Template of pipeline using [cgatcore][link-cgatcore].

[link-cgatcore]: https://github.com/cgat-developers/cgat-core

## Usage

### Running the pipeline

- [ ] Clone the new repository to the computer where you wish to run the pipeline.
- [ ] Create a Conda environment named `pipeline-env` using the file `environment.yml`. 
- [ ] Run the pipeline!
  + On a High-Performance Computing (HPC) cluster, `python pipeline.py make full -v 5`, to use the Distributed Resource Management Application API (DRMAA).
  + On a local machine `python pipeline.py make full -v 5 --local`.

### Using the pipeline as a template for new pipelines

- [ ] Create a new repository from this one, using the `Use as template` button on [GitHub](https://github.com/sims-lab/pipeline_rnaseq_hisat2).
  + That way, your new repository starts its own commit history, where you can record your own changes!
  + Only fork this repository if you wish to contribute updates to the template pipeline itself.
- [ ] Clone the new repository to the computer where the pipeline will be run.
- [ ] Edit the file `pipeline.py` to define the pipeline workflow.
  + [ ] Add import statements to the `Imports` section.
  + [ ] Edit the `Configuration` as needed, if needed.
  + [ ] Replace the `Workflow` section with your own pipeline steps.
  + The `Main execution` section should be left as-is
- [ ] Edit the file `environment.yml` to define a Conda environment for running this pipeline.
- [ ] Edit the configuration of the pipeline as needed, in the file `config.yml`.
- [ ] Edit the configuration of the pipeline as needed, in the file `config.yml`.
- [ ] Run the pipeline!
  + On a High-Performance Computing (HPC) cluster, `python pipeline.py make full -v 5`, to use the Distributed Resource Management Application API (DRMAA).
  + On a local machine `python pipeline.py make full -v 5 --local`.
