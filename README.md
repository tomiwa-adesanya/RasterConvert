# RasterConvert - Raster Image file format converter

![rasterconvert](/data/img/rasterconvert.png)

## Description

RasterConvert is a Windows OS application that can be used to seamlessly convert Raster images from one file format to another. 

Raster images are images compiled using pixels, or tiny dots, containing unique color and tonal information that come together to create the image.
Examples of raster image file formats include PNG, TIFF, DIB, JPEG, GIF, EPS e.t.c.   

Raster images file format formats supported by RasterConvert are:
  * PNG (Portable Network Graphics)
  * JPEG (Joint Photographic Experts Group)
  * ICO (Windows Icon)
  * TIFF (Tag Image File Format)
  * DIB (Device Independent Bitmap)
  * GIF (Graphics Interchange Format)

RasterConvert also maintains image transparency in file formats that support transparent background such as PNG, TIFF, GIF, ICO.

## Working with the source code(Python programmers)

RasterConvert was written in Python, and the source code to this project can be found [here](/main.py)

Requirments:  

   * Windows OS.
   * Python version 3.9 or higher.
   * Python third party library `PIL`.
        * To install `PIL`, in your Windows terminal enter `pip install pillow`.
   * An IDE, preferably VS-Code or PyCharm
   
Clone this repository unto your computer, and run *main.py*. 
 
## Installing and running RasterConvert(Non Python Programmers)
 
For non-programmers, I have compiled and included a setup that may be installed unto your computer before running application.
Upon installation of setup, RasterConvert application shortcut will be added to your start menu and desktop. I have also included a  standalone executable that doesn't require installation before running application.
 
To install RasterConvert setup, first of all download it from [here](/data/dist/RasterConvert-setup.exe).
Run RasterConvert-setup after downloading it, and follow the steps provided by the setup for proper installation.

If you'd prefer to run the standalone application without installation, download the [zipped package](/data/dist/RasterConvert.zip). Unzip the files of the downloaded zipped package into any folder of your choice in your computer. Within the unzipped files, search for *RasterConvert.exe* and double click it to run the RasterConvert application directly.

## How to use RasterConvert to convert 

RasterConvert provides users an easy-to-use graphical interface that can be used effortlessly without a guide, but following this section includes a guide on how to go about interacting with the interface.

RasterConvert user interface preview:

  ![RasterConvert-preview](/data/img/preview/preview.png)

STEP 1:

  Click on the `select image` button. A filedialog would be created to enable you choose the image you want to convert. The path to the image would be displayed in the disabled text area.

  ![step-1](/data/img/preview/step-1.png)
  ![step-1-a](/data/img/preview/step-1-a.png)

STEP 2:

  Select the file format you want to convert the selected image to, and click the `convert` button to start conversion. 
  By default, the converted image would be saved in your computer's *download* folder. If the download folder path is unavailable, you'd be prompted to choose a different folder and name to save the conversion output. Upon completion of image conversion, a message dialog would be created to give you a response to successful conversion before opening the folder the converted image was stored in.

  ![step-2](/data/img/preview/step-2.png)
  ![response](/data/img/preview/response.png)