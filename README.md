# Releaser

[![Lint](https://github.com/cledouarec/releaser/actions/workflows/lint.yaml/badge.svg)](https://github.com/cledouarec/releaser/actions/workflows/lint.yaml)
[![Unit tests](https://github.com/cledouarec/releaser/actions/workflows/test.yaml/badge.svg)](https://github.com/cledouarec/releaser/actions/workflows/test.yaml)

**Table of Contents**
* [Overview](#Overview)
* [Installation](#Installation)
* [Usage](#Usage)
* [Configuration](#Configuration)

## Overview


**Releaser** is a module and a script used to provide swiss knife to release
management. It provides several tools to interact with Atlassian tools
Confluence and Jira.

## Installation

### From PyPI (Recommended)

You can install easily with the following command or insert into your
requirements file :
```
pip install releaser
```

### From sources

It is recommended to use a virtual environment :
```
python -m venv venv
```
To install the module and the main script, simply do :
```
pip install .
```
For the developers, it is useful to install extra tools like :
* [pre-commit](https://pre-commit.com)
* [pytest](http://docs.pytest.org)

These tools can be installed with the following command :
```
pip install '.[dev]'
```
The Git hooks can be installed with :
```
pre-commit install
```
The hooks can be run manually at any time :
```
pre-commit run --all-file
```

## Usage

The script with required argument can be started by executing the following
command :
```
./releaser my_config.yaml
```

The full list of arguments supported can be displayed with the following
helper :
```
./releaser.exe -h
TBC
```

## Configuration

The configuration file support 2 formats :
- [YAML format](https://yaml.org) (Recommended format)
- [JSON format](https://www.json.org)

**_In Yaml :_**
```yaml
Server:
  Jira: "https://my.jira.server.com"
```
**_In Json :_**
```json
{
  "Server": {
    "Jira": "https://my.jira.server.com"
  }
}
```

### Server configuration

The `Server` node will configure the URL of the Jira server.
For the moment, only the username/password authentication is supported but only
in the command line for security reason.

**_In Yaml :_**
```yaml
Server:
  Jira: "https://my.jira.server.com"
```
**_In Json :_**
```json
{
  "Server": {
    "Jira": "https://my.jira.server.com"
  }
}
```

#### Server

Main configuration node for server.  
**It is a mandatory field.**

#### Jira

Define the Jira server URL to retrieve the information to extract.  
**It is a mandatory field.**
