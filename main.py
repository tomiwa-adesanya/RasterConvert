from PIL import Image 
from tkinter import ttk
from tkinter import filedialog
from os import getlogin, path, startfile
from tkinter.messagebox import showerror, showinfo
import tkinter as tk

icon_path = "data\\img\\icon.ico"

class RasterConvert(tk.Tk):
    def __init__(self):
        super().__init__() # Calling tk.Tk() constructor

        #--------------------------------------------------------------------------
        #-------------------ROOT WINDOW CONFIGURATION------------------------------
        #--------------------------------------------------------------------------
        self.title("RasterConvert")
        self.geometry("550x200")
        self.attributes("-alpha", 0.95)
        self.resizable(False, False)
        self.iconbitmap(icon_path)

        self.main_frame = ttk.Frame(self, relief="ridge",)
        self.main_frame.pack(
            expand=True, fill="both", padx=5, pady=5
        )

        #-------------------------------------------------------------------------
        #----------------------------ATTRIBUTES-----------------------------------
        #-------------------------------------------------------------------------
        login = getlogin()
        self._initialdir = f"C:\\Users\\{login}\\pictures"
        self.filetypes = (
            ( "image files", "*.png"),
            ("image files", "*.gif"),
            ("image files", "*.jpeg"),
            ("image files", "*.jpg"),
            ("image files", "*.jpe"),
            ("image files", "*.jfif"),
            ("image files", "*.tif"),
            ("image files", "*.tiff"),
            ("image files", "*.hif"),
            ("image files", "*.dib"),
            ("image files", "*.ico")
        )
        self.img_path = ""
        self.savepath = f"C:\\Users\\{login}\\downloads"
        #---------------------------------------------------------------------------
        #---------------------------------------------------------------------------
        self.__build_components()
        self.__bind_events() 
        self.mainloop()

    def __build_components(self) -> None:
        
        Button = ttk.Button
        Entry = ttk.Entry
        Frame = ttk.Frame
        Label = ttk.Label
        Radiobutton = ttk.Radiobutton
        StringVar = tk.StringVar

        self.img_path_var = StringVar()
        self.format_var = StringVar()

        entry_grid_config = {
            "ipadx" : 110, "ipady" : 7.5,  "padx" : 2.5, "sticky" : "nw", 
        }
        button_grid_config = {
            "ipady" : 7.5, "sticky" : "nw"
        }

        #---------------------------------------------------------------------------------------------
        #-------------------------------IMAGE PATH SECTION CONFIG-------------------------------------
        #---------------------------------------------------------------------------------------------
        image_path_entry = Entry(
            self.main_frame, textvariable=self.img_path_var, font=("Helvetica", 12), state="disabled"
        )
        image_path_entry.grid(
            column=0, row=0, columnspan=2, pady=15,**entry_grid_config
        )
        self.img_path_var.set("select image path")

        image_select_path_button = Button(
            self.main_frame, text="select image", command=lambda: self.get_img_path()
        )
        image_select_path_button.grid(
            column=2, row=0, pady=15, ipadx=22.5, **button_grid_config
        )
        #----------------------------------------------------------------------------------------
        #-----------------------------RADIOBUTTON SECTION----------------------------------------
        #----------------------------------------------------------------------------------------
        radiobuttons_frame = Frame(
            self.main_frame
        )
        radiobuttons_frame.grid(
            column=0, row=1, columnspan=3, rowspan=2, sticky="nw", padx=2.5, pady=3.5, 
        )

        radiobutton_descr = Label(
            radiobuttons_frame, text="convert to:", font=("Helvetica", 15)
        )
        radiobutton_descr.grid(
            column=0, row=0, padx=2.5, pady=2.5, stick="w"
        )
        # PNG RADIOBUTTON
        png_radiobutton = Radiobutton(
            radiobuttons_frame, text="PNG", value="png", variable=self.format_var
        )
        png_radiobutton.grid(
            column=1, row=0, sticky="w", padx=15
        )
        # ICO RADIOBUTTON
        ico_radiobutton = Radiobutton(
            radiobuttons_frame, text="ICO", value="ico", variable=self.format_var
        )
        ico_radiobutton.grid(
            column=2, row=0, sticky="w", 
        )
        # GIF RADIOBUTTON
        gif_radiobutton = Radiobutton(
            radiobuttons_frame, text="GIF", value="gif", variable=self.format_var
        )
        gif_radiobutton.grid(
            column=3, row=0, sticky="w",  padx=15
        )
        # JPEG RADIOBUTTON
        jpg_radiobutton = Radiobutton(
            radiobuttons_frame, text="JPEG", value="jpeg", variable=self.format_var
        )
        jpg_radiobutton.grid(
            column=4, row=0, sticky="w", 
        )
        # TIFF RADIOBUTTON
        tiff_radiobutton = Radiobutton(
            radiobuttons_frame, text="TIFF", value="tiff", variable=self.format_var
        )
        tiff_radiobutton.grid(
            column=5, row=0, sticky="w",  padx=15
        )
        # DIB RADIOBUTTON
        dib_radiobutton = Radiobutton(
            radiobuttons_frame, text="DIB", value="dib", variable=self.format_var
        )
        dib_radiobutton.grid(
            column=6, row=0, sticky="w", 
        )

        #----------------------------------------------------------------------------------------
        #---------------------------------CONVERT BUTTON-----------------------------------------
        #----------------------------------------------------------------------------------------
        convert_button = Button(
            self.main_frame, text="convert", command=lambda: self.convert()
        )
        convert_button.grid(
            row=3, columnspan=3, ipadx=15, ipady=13, pady=25
        )
    
    def get_img_path(self) -> None:
        """
        Creates a filedialog that enables users to select the image to be converted on their computer
        """
        self.img_path = filedialog.askopenfilename(
            title="open image",
            initialdir=self._initialdir,
            filetypes=self.filetypes
        )
        if (self.img_path):
            self.img_path_var.set(self.img_path)
    
    def get_destination(self) -> str:
        """
        Creates a filedailog that enables user to enter name the converted image is to be saved as in a specified directory
        """
        path = filedialog.asksaveasfilename(
            title="save image as",
            initialdir=self._initialdir,
            filetypes=self.filetypes
        )
        return path

    def convert(self) -> None:

        if (self.savepath and self.img_path and self.format_var):
            _format = self.format_var.get()
            file_name = path.basename(self.img_path).split(".")[0] + f".{_format}"    
            destination = self.savepath + "\\" + file_name

            img = Image.open(self.img_path)
            img_format = img.format

            if (_format == "jpeg"):
                img = img.convert("RGB")
            elif (_format == "ico"):
                return self.convert_ico(img, img_format, destination)
            elif (not _format):
                _format = "png"

            try:
                img.save(destination, format=_format)
                startfile(self.savepath)
            except:
                destination = self.get_destination() + f".{_format}"
                img.save(destination, format=_format)
            finally:
                showinfo(
                    title="Image conversion",
                    message=f"{img_format} to {_format} conversion completed"
                )
                dir = path.dirname(destination)
                startfile(dir)

        else:
            showerror(
                title="RascalConvert error",
                message="Please select both the image and the file format to convert the image to"
            )

    def convert_ico(self, img: Image.Image, img_format:str,  destination: str) -> None:
        """
        Converts other image types to an ico
        """
        _sizes = [(128, 128), (256, 256)]
        img = img.resize([max(img.size)] * 2)
        try:
            img.save(destination, format="ico", sizes=_sizes)
            startfile(destination)
        except:
            destination = self.get_destination() + f".ico"
            img.save(destination, format="ico", sizes=_sizes)
        finally:
            showinfo(
                title="Image conversion",
                message=f"{img_format} to ICO conversion completed"
            )
            dir = path.dirname(destination)
            startfile(dir)
        
    def __bind_events(self) -> None:
        self.bind(
            "<Control-w>", lambda event=None: self.destroy()
        )
        self.bind(
            "<Control-W>", lambda event=None: self.destroy()
        )
            
RasterConvert()