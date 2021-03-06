# bpyd2

A Python library for creating data driven scenes in Blender.

The API is documented [here](bpyd2.md).

## Pre-requisites

  - Python 3.9.2 or greater
  - Blender 2.93.5 or greater
  
## Dependencies

Outside of the core Python libraries, the only dependency is the `bpy` library which forms the core API of Blender. If you are working with bpyd2 inside Blender, this will already be there. For testing / development purposes,

```Shell
python -m pip install bpy
```

## Installation

```Shell
python -m pip install git+https://github.com/adamml/bpyd2.git
```

## Gallery and examples

### Wave heights around Ireland

|[]()| |
|----|----|
|![Wave heights around Ireland](./gallery/wave_and_weather_buoys.png) | [![Alt text](https://img.youtube.com/vi/4Z14M2PZc9U/0.jpg)](https://www.youtube.com/watch?v=4Z14M2PZc9U) |

### World marathon majors elevation plots

![World Marathon Majors elevation](./gallery/abott_wmm.png)

## Building the documentation

The documentation for the module is generated with pdoc-markdown:

```Shell
pydoc-markdown -I . -m bpy2d --render-toc > bpyd2.md
```