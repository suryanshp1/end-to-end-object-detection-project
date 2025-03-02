# end-to-end-object-detection-project

A simple project to detect sign language . 
Uploaded training images to https://app.roboflow.com/ and did manual annotation (then create and download dataset in YOLOV5 PyTorch format).


## Workflows

- constants
- config_entity
- artifact_entity
- components
- pipeline

## How to run ?

make sure to install anaconda before running these commands

```bash
conda create -n signlangvenv python=3.10 -y
```

```bash
conda activate signlangvenv
```

```bash
pip install -r requirements.txt
```

```bash
python app.py
```

Alternatively, You can also use make commands

```bash
make create-env
```

```bash
make install
```

```bash
make run
```

```bash
make clean
```