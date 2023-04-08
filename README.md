# MQHAD<!-- omit from toc -->

Munich Quantum HArdware Designer (MQHAD) is a framework to encapsulate application-driven quantum hardware architecture.In this repository, a reference implementation of the framework is provided. This implementation was done with modularality and easy extensibility in mind to allow for future extensions and improvement.

## Table of contents<!-- omit from toc -->

- [Steps in framework](#steps-in-framework)
- [Repository structure](#repository-structure)
- [Extending reference implementation](#extending-reference-implementation)
  - [Architecture generator](#architecture-generator)
  - [Physical layout mapper](#physical-layout-mapper)
  - [Optimizer](#optimizer)
- [Trying reference implementation](#trying-reference-implementation)
  - [Installation](#installation)
    - [Installing Package](#installing-package)
    - [Installing Qiskit Metal](#installing-qiskit-metal)
  - [Usage](#usage)
    - [Command-line interface (CLI)](#command-line-interface-cli)
    - [Testing the Package](#testing-the-package)
  - [Development](#development)
  - [FAQs](#faqs)


## Steps in framework

In this section, we will describe the steps in the framework as follows:

1. `Architecture generator` - generates an optimized high-level architecture based on a quantum application(i.e, quantum circuit). The input of the architecture generator is a quantum application and it outputs a high-level architecture containing the layout of the qubits and qubit frequencies
2. `Physical layout mapper` - maps the high-level architecture to physical layout using tools such as Qiskit Metal
3. `Statistical model` - trains statistical models to stand-in for simulations that are done using software such as Ansys HFSS during the optimization step. The models are trained separately from the design flow using pre-collected simulation data. The models identify patterns that relates a target parameter to the geometrical parameters of the layout.
4. `Optimizer` - optimizes layout using statistical model created in (3). Usually, the optimization of physical layout process needs iterative simulation and adjustment of geometries of the physical layout. Since, pre-trained statistical models are being used to stand-in for the simulation softwares, geometrical value for a targeted parameter can be obtained without needing iterative simulation and design

## Repository structure

In this section, we will describe the structure of the repository as follows to help you navigate through the repository:

1. `mqhad` - contains the reference implementation of the framework covering the modules in steps 1,2, and 4 in the previous section
   1. `architecture_generator1` is based on [G. Li, Y. Ding and Y. Xie](https://arxiv.org/abs/1911.12879)
      1. `bus` generates connection between qubits
      2. `chip` creates temporary chip for simulation. The temporary chip is a subgraph of the layout graph and it is used in the frequency generation module
      3. `frequency` generates frequency of qubits using Monte Carlo simulation. It chooses frequency configuration based on maximum yield rate as computed by the `yieldsimulator` module
      4. `layout` generates matrix of qubit layout
      5. `profile` generates profiles of quantum application. The profile of are as follows:
         1. Two qubit gate map which contains control and target gates of the two qubit gate
         2. Connectivity degree of qubits
         3. Adjacency matrix of qubit
      6. `yieldsimulator` calculates the yield rate that is used by the `frequency` module. Yield rate is the number of sub-graphs with no frequency collision divided by the number of trials
   2. `mapper` maps architecture generator layout to [Qiskit Metal](https://qiskit.org/documentation/metal/) physical layout
      1. `canvas` is a module that creates the design space for the physical layout
      2. `capacitor` creates the capacitors
      3. `capacitor_launchpad_connector` generates capacitor to launchpad connectors
      4. `launchpad` creates launchpads(i.e, readout/control)
      5. `qubit` creates qubits
      6. `qubit_capacitor_connector` creates qubit to capacitor connections
      7. `qubit_connector` creates qubit-to-qubit connections
   3. `optimizer` optimizes the geometries of layout to hit target parameters
2. `notebooks` trains statistical model to stand-in for simulation software such as Ansys HFSS and used by the optimizer

## Extending reference implementation

In this section, we will describe how to extend the reference implementation to include other modules in the framework. The script that integrates the different steps is defined in [__main__.py](mqhad/__main__.py). In the following sub-sections, we will describe how to replace the modules in the reference implementation with other modules.

### Architecture generator

The architecture generator shown below can be replaced with other solutions that can generate a matrix of qubit layout and its associated qubit frequencies.

```
qc = QuantumCircuit.from_qasm_file(circuit_absolute_path)
generator = Generator(qc=qc)
qubit_grid, qubit_frequencies = generator.generate()
```

### Physical layout mapper

The mapper module shown in below can be replaced with other implementations than Qiskit Metal provided that they have an Application Programming Interface (API) to update the layout that can be used in the optimizer step.

```
mapper = Mapper(
    design_backend="metal",
    qubit_grid=qubit_grid,
    qubit_frequencies=qubit_frequencies
)
result = mapper.map()
```

### Optimizer

The optimizer shown below can be replaced with other optimizer algorithms. If the goal is to replace just the the statistical model provided to the optimizer module, then, the path to different models can be given in the configuration file.

```
canvas = result["canvas"]
optimizer = Optimizer(
    canvas=canvas, 
    qubit_frequencies=qubit_frequencies, 
    config=config
)
optimizer.optimize()
```

## Trying reference implementation

### Installation

#### Installing Package

1. Clone the repository - `git clone {URL}`

2. Change to cloned directory - `cd mqhad`

3. The easiest way to install the toolkit without affecting other packages is to create a virtual environment, i.e: using conda, as following. Else, you can just run `python -m pip install -e .`. Do note that MQHAD is tested on Python 3.10.

```text
conda env create -n <env_name> environment.yml
conda activate <env_name>
python -m pip install --no-deps -e .
```

#### Installing Qiskit Metal

1. Install Qiskit Metal following installation instructions at [Qiskit Metal](https://qiskit.org/documentation/metal/installation.html). Refer to the [Pre-existing environment](https://qiskit.org/documentation/metal/installation.html#option-2-a-pre-existing-environment) section.

### Usage

#### Command-line interface (CLI)

```text
Usage:
    mqhad --file-path [PATH_TO_QASM_2.0_FILE] --config-file-path [PATH_TO_CONFIG_FILE]
```

The CLI will generate the high-level architecture of the placement of qubits in a 2D square-lattice and the corresponding qubit frequencies. The Metal GUI is invoked at the end as following where there is an option to save the design as a Python script.

![4_qubit_2D_square_lattice](docs/images/4_qubit_2D_square_lattice.png)

#### Testing the Package

1. There is a test circuit that could be used to test the package. Navigate to `mqhad` directory and execute `mqhad --file-path ./mqhad/tests/test_circuit/circuit1.qasm --config-file-path ./mqhad/tests/test_config/config.yml`

### Development

1. On top of normal installation, install development dependencies using `pip install -r requirements-dev.txt`

### FAQs

- QT Warnings

>From [Qiskit Metal FAQ](https://qiskit.org/documentation/metal/faq.html):
>
>Q: Why am I seeing a critical error from qt about not controlling layer-backing?
>
>A: If you are seeing: CRITICAL [_qt_message_handler]: …. WARNING: Layer-backing can not be explicitly controlled on 10.14 when built against the 10.14 SDK … you are likely running a MAC OS version that has trouble with the libraries. Based on information that is available online, this problem does not appear to have a solution. However, it does not seem like this error affects Qiskit Metal’s functionality. If you find problem with this, you might want to try using an older version of the dependency packages, beginning with lowering your python version to 3.7.x.
