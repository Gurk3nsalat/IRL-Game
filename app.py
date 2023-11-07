import customtkinter
import time

from frames.SimpleExampleFrame import SimpleExampleCtkFrame
from frames.ComplexExampleFrame import ComplexExampleCtkFrame

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("1280x720")
        self.title("Tom's IRL Game")

        self.simple_example_frame = SimpleExampleCtkFrame(master=self)
        self.complex_example_frame = ComplexExampleCtkFrame(master=self)

        self.frame_list = [self.simple_example_frame, self.complex_example_frame]
        self.last_index = None
        self.current_index = 0
        self.current_frame = None

    def switch_frame(self):
        if self.last_index is not None:
            self.current_frame.forget()

        self.last_index = self.current_index

        self.current_frame = self.frame_list[self.current_index]
        self.current_frame.pack(pady=20, padx=60, fill="both", expand=True)
        self.current_index += 1

        if self.current_index >= len(self.frame_list):
            self.current_index = 0
            self.last_index = len(self.frame_list) -1



if __name__ == '__main__':
    app = App()
    app.switch_frame()
    time.sleep(3)
    app.switch_frame()
    app.mainloop()
