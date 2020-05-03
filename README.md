# Mavic Pro conversion tool DNG to PNG

Conversion tool for DNG rawfiles  Mavic Pro into PNG files.

## Installing requirements

It's required python version ≥ 3 and pip. Install then the required packages:

```bash
pip3 install -r requirements.txt
```

## Usage

You have two ways to run this script.

Either put *convert.py* into the folder where DNG files are and then run ```python3 convert.py```. It will be asked you to specify the destination, whose default value is *./PNG* .

Otherwise, you can specify a source path (and a destination path) running ```python3 convert.py --source /source/path --destination /destination/path```. If the destination path does not exists, it will be asked you to confirm to create it. If you don't specify it, its deafult value is again */source/path/PNG* .

Enjoy.

[Follow me!](https://github.com/glofru)

