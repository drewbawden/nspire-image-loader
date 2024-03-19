# nspire-images

nspire-images is a program to create a .tns document that displays an image on a TI-Nspire CX II calculator

I made this program because I wanted to load images on my graphing calculator but the non-CAS version doesn't suport images

## Installation & Usage
#### Installation
```
git clone https://github.com/drewbawden/nspire-images.git
```

#### Usage
```
python parseImage.py -i <input file> -o <output file> -s <output resolution>
```

#### Example
```
python parseImage.py -i input.png -o output.lua -s 200x250
```

#### Load Image

The program will create a .lua file that contains code that must be pasted in the TI-Nspire script editor

This will require the [TI-Nspire Student Software](https://education.ti.com/en/software/details/en/A78091CD540843D68AB8EE5853C84828/student-nspirecx) 

To paste the script you need to create a new document, click insert and insert new script. Then paste in the code and save the document.

