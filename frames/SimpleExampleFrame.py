import customtkinter

class SimpleExampleCtkFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.label_1 = customtkinter.CTkLabel(master=self, justify=customtkinter.LEFT)
        self.label_1.pack(pady=10, padx=10)

        self.progressbar_1 = customtkinter.CTkProgressBar(master=self)
        self.progressbar_1.pack(pady=10, padx=10)

        self.button_1 = customtkinter.CTkButton(master=self, command=self.button_callback)
        self.button_1.pack(pady=10, padx=10)

        self.slider_1 = customtkinter.CTkSlider(master=self, command=self.slider_callback, from_=0, to=1)
        self.slider_1.pack(pady=10, padx=10)
        self.slider_1.set(0.5)

        self.entry_1 = customtkinter.CTkEntry(master=self, placeholder_text="CTkEntry")
        self.entry_1.pack(pady=10, padx=10)

        self.optionmenu_1 = customtkinter.CTkOptionMenu(self,
                                                        values=["Option 1", "Option 2", "Option 42 long long long..."])
        self.optionmenu_1.pack(pady=10, padx=10)
        self.optionmenu_1.set("CTkOptionMenu")

        self.combobox_1 = customtkinter.CTkComboBox(self,
                                                    values=["Option 1", "Option 2", "Option 42 long long long..."])
        self.combobox_1.pack(pady=10, padx=10)
        self.combobox_1.set("CTkComboBox")

        self.checkbox_1 = customtkinter.CTkCheckBox(master=self)
        self.checkbox_1.pack(pady=10, padx=10)

        self.radiobutton_var = customtkinter.IntVar(value=1)
        self.radiobutton_1 = customtkinter.CTkRadioButton(master=self, variable=self.radiobutton_var, value=1)
        self.radiobutton_1.pack(pady=10, padx=10)
        self.radiobutton_2 = customtkinter.CTkRadioButton(master=self, variable=self.radiobutton_var, value=2)
        self.radiobutton_2.pack(pady=10, padx=10)

        self.switch_1 = customtkinter.CTkSwitch(master=self)
        self.switch_1.pack(pady=10, padx=10)

        self.text_1 = customtkinter.CTkTextbox(master=self, width=200, height=70)
        self.text_1.pack(pady=10, padx=10)
        self.text_1.insert("0.0", "CTkTextbox\n\n\n\n")

        self.segmented_button_1 = customtkinter.CTkSegmentedButton(master=self,
                                                                   values=["CTkSegmentedButton", "Value 2"])
        self.segmented_button_1.pack(pady=10, padx=10)

        self.tabview_1 = customtkinter.CTkTabview(master=self, width=300)
        self.tabview_1.pack(pady=10, padx=10)
        self.tabview_1.add("CTkTabview")
        self.tabview_1.add("Tab 2")

    def button_callback(self):
        print("Button click", self.combobox_1.get())

    def slider_callback(self, value):
        self.progressbar_1.set(value)