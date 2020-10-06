import tkinter as tk
import json

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master=None)
        self.master = master
        self.pack()
        self.create_textFields()
        self.create_widgets()

    def create_textFields(self):
        self.date_label = tk.Label(self,text="Date:")
        self.text_field_date = tk.Entry(self)
        self.death_label = tk.Label(self,text="Death:")
        self.text_field_death = tk.Entry(self)
        self.tests_label = tk.Label(self,text="Tests:")
        self.text_field_tests = tk.Entry(self)
        self.cases_label = tk.Label(self,text="Cases:")
        self.text_field_cases = tk.Entry(self)
        self.date_label.pack()
        self.text_field_date.pack()
        self.tests_label.pack()
        self.text_field_tests.pack()
        self.cases_label.pack()
        self.text_field_cases.pack()
        self.death_label.pack()
        self.text_field_death.pack()

    def create_widgets(self):
        self.submit = tk.Button(self,text="submit",command=self.update_JSON)
        self.submit.pack()
        
        self.quit = tk.Button(self, text="quit",fg="red",command=self.master.destroy)
        self.quit.pack(side="bottom")
    
    def update_JSON(self):
        with open("cases.json") as file:
            data = json.load(file)
        
        temp = data["tests"]
        new_record = {
            "date":self.text_field_date.get(),
            "number_of_tests":self.text_field_tests.getint(),
            "number_of_new_cases":self.text_field_cases.getint(),
            "death":self.text_field_death.getint()
        }

        temp.append(new_record)

        with open("test.json",'w') as test_file:
            json.dump(data,test_file)


root = tk.Tk()
app = App(master=root)
app.mainloop()





