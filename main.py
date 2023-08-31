import tkinter as tk
from tkinter import filedialog as fd
import os
from Solar_API_Call import solar_api_call

class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Solar Analysis Platform").pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Open Solar Optimization Program",
                  command=lambda: master.switch_frame(SolarOp)).pack(padx=5, pady=5)
        tk.Button(self, text="Instructions",
                  command=lambda: master.switch_frame(PageTwo)).pack(padx=5, pady=5)


class SolarOp(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Button(self, text="Return to start page",
                  command=lambda: master.switch_frame(StartPage)).grid(row=10, column=0, padx=5, pady=5)

        # initate string_vars
        weather_var = tk.StringVar(master=self, value="")


        def split_filepath(filepath):
            """
            :param filepath:
            :return:just the filename at the end of the filepath
            """
            filename = filepath.split("/")[-1]
            return filename

        def select_weather_file():
            # this will update a global variable of fpm_filepath with a selected file
            # this is not the right way to do this, but I can't figure out a better way for now
            filetypes = (
                ('text files', '*.csv'),
                ('data files', '*.dat'),
                ('All files', '*.*')
            )
            cwd = os.getcwd()
            weather_var.set(fd.askopenfilename(
                title='Open a file',
                initialdir=os.path.join(cwd, "Solar_API_Call", "inputs"),
                filetypes=filetypes))
            # split the text file name
            label_value = split_filepath(weather_var.get())
            tk.Label(self, text=label_value).grid(row=0, column=1, columnspan=2)

        tk.Button(self, text="Select Weather File", command=select_weather_file).grid(row=0, column=0)
        tk.Button(self, text="Select Location", command=None).grid(row=1, column=0)
        tk.Button(self, text="Select Edit Params", command=None).grid(row=2, column=0)
        tk.Button(self, text="Select API Key", command=None).grid(row=3, column=0)

        # GCR range input
        tk.Label(self, text="Enter GCR Range:").grid(row=4, column=0)
        tk.Entry(self, width=30).grid(row=4, column=1)
        tk.Label(self, text="to").grid(row=4, column=2)
        tk.Entry(self, width=30).grid(row=4, column=3)

        # DC/AC range input
        tk.Label(self, text="Enter DC/AC Range:").grid(row=5, column=0)
        tk.Entry(self, width=30).grid(row=5, column=1)
        tk.Label(self, text="to").grid(row=5, column=2)
        tk.Entry(self, width=30).grid(row=5, column=3)

        # run solar api call module
        tk.Button(self, text="Run API Program", command=solar_api_call.main(weather_var.get())).grid(row=10, column=3)



class PageTwo(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="This will be instructions! Not Ready Yet").pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Return to start page",
                  command=lambda: master.switch_frame(StartPage)).pack(padx=5, pady=5)


if __name__ == "__main__":
    app = SampleApp()
    app.title("Solar Analysis Platform")
    app.geometry("700x300")
    app.mainloop()

