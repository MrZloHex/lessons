#################################################################
#   Programm for timetable                                      #
#      begin of developing                                      #
#          5.10.2020                                            #
#                       version beta 0.0.2                      #
#                                                               #
#                      by MrZlo                                 #
#################################################################


import tkinter as tk
from tkinter import ttk
import sqlite3 as sql

day_db = 'lessons_mon'

class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.db = db
        day_db = 'lessons_mon'
        self.view_records(day_db)

    def init_main(self):
        toolbar = tk.Frame(bd=5)
        toolbar.pack(side=tk.TOP, fill=tk.X)
        daybar = tk.Frame(bd=5)
        daybar.pack(side=tk.TOP, fill=tk.X)

        self.lesson_add_img = tk.PhotoImage(file="img\lesson_add.gif")
        btn_add_lesson = tk.Button(toolbar, command=self.add_lesson, bd=1, compound=tk.TOP, image=self.lesson_add_img)
        btn_add_lesson.pack(side=tk.LEFT)
        self.quit_img = tk.PhotoImage(file='img\quit.gif')
        btn_quit = tk.Button(toolbar, command=self.quit, bd=1, compound=tk.TOP, image=self.quit_img)
        btn_quit.pack(side=tk.RIGHT)

        btn_mon = tk.Button(daybar, command=self.mon_db, bd=1, compound=tk.TOP, text='Monday')
        btn_mon.pack(side=tk.LEFT)
        btn_tues = tk.Button(daybar, command=self.tues_db, bd=1, compound=tk.TOP, text='Tuesday')
        btn_tues.pack(side=tk.LEFT)
        btn_wed = tk.Button(daybar, command=self.wed_db, bd=1, compound=tk.TOP, text='Wednesday')
        btn_wed.pack(side=tk.LEFT)
        btn_thurs = tk.Button(daybar, command=self.thurs_db, bd=1, compound=tk.TOP, text='Thursday')
        btn_thurs.pack(side=tk.LEFT)
        btn_fri = tk.Button(daybar, command=self.fri_db, bd=1, compound=tk.TOP, text='Friday')
        btn_fri.pack(side=tk.LEFT)

        self.tree = ttk.Treeview(self, columns=('number_lesson', 'name_lesson', 'begin_lesson', 'end_lesson'), show='headings')
        self.tree.column('number_lesson', width=30, anchor=tk.CENTER)
        self.tree.column('name_lesson', width=300, anchor=tk.CENTER)
        self.tree.column('begin_lesson', width=150, anchor=tk.CENTER)
        self.tree.column('end_lesson', width=150, anchor=tk.CENTER)
        self.tree.heading('number_lesson', text='№')
        self.tree.heading('name_lesson', text='Lesson')
        self.tree.heading('begin_lesson', text='Begins at')
        self.tree.heading('end_lesson', text='Ends at')
        self.tree.pack()

    def records(self, number_lesson, name_lesson, begin_lesson, end_lesson, day_db):
        self.db.insert_data(number_lesson, name_lesson, begin_lesson, end_lesson, day_db)
        self.view_records(day_db)

    def view_records(self, day_db):
        self.conn = sql.connect('lessons.db')
        self.db.c.execute('''CREATE TABLE IF NOT EXISTS %s (number_lesson integer primary key, name_lesson text, begin_lesson text, end_lesson text)''' % day_db)
        self.conn.commit()
        self.db.c.execute('''SELECT * FROM %s''' % day_db)
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def mon_db(self):
        day_db = 'lessons_mon'
        self.view_records(day_db)
    def tues_db(self):
        day_db = 'lessons_tues'
        self.view_records(day_db)
    def wed_db(self):
        day_db = 'lessons_wed'
        self.view_records(day_db)
    def thurs_db(self):
        day_db = 'lessons_thurs'
        self.view_records(day_db)
    def fri_db(self):
        day_db = 'lessons_fri'
        self.view_records(day_db)

    def add_lesson(self):
        Add_Lesson()

    def quit(self):
        Quit()

class Add_Lesson(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_add_lesson()
        self.view = app
        self.db = db

    def init_add_lesson(self):
        self.title('Add lesson')
        self.geometry("300x190+400+300")
        self.resizable(False, False)
        self.grab_set()
        self.focus_set()

        label_number_lesson = ttk.Label(self, text='Number of lesson:')
        label_number_lesson.place(x=20, y=20)
        label_name_lesson = ttk.Label(self, text='Name of lesson:')
        label_name_lesson.place(x=20, y=50)
        label_begin_lesson = ttk.Label(self, text='Begining of lesson:')
        label_begin_lesson.place(x=20, y=80)
        label_end_lesson = ttk.Label(self, text='Ending of lesson:')
        label_end_lesson.place(x=20, y=110)
        label_begin_lesson_t = ttk.Label(self, text=':')
        label_begin_lesson_t.place(x=221, y=80)
        label_end_lesson_t = ttk.Label(self, text=':')
        label_end_lesson_t.place(x=221, y=110)

        self.entry_number_lesson = ttk.Entry(self, width=17)
        self.entry_number_lesson.place(x=170, y=20)
        self.entry_name_lesson = ttk.Entry(self, width=17)
        self.entry_name_lesson.place(x=170, y=50)
        self.entry_begin_lesson_h = ttk.Entry(self, width=5)
        self.entry_begin_lesson_h.place(x=170, y=80)
        self.entry_begin_lesson_m = ttk.Entry(self, width=5)
        self.entry_begin_lesson_m.place(x=242, y=80)
        self.entry_end_lesson_h = ttk.Entry(self, width=5)
        self.entry_end_lesson_h.place(x=170, y=110)
        self.entry_end_lesson_m = ttk.Entry(self, width=5)
        self.entry_end_lesson_m.place(x=242, y=110)

        btn_add = tk.Button(self, text='Add', command=self.destroy)
        btn_add.place(x=200, y=150)
        btn_add.bind('<Button-1>', self.get_data)
        btn_close = tk.Button(self, text='Close', command=self.destroy)
        btn_close.place(x=239, y=150)

    def get_data(self, event):
        begin_lesson = self.entry_begin_lesson_h.get() + ':' + self.entry_begin_lesson_m.get()
        end_lesson = self.entry_end_lesson_h.get() + ':' + self.entry_end_lesson_m.get()
        self.view_records(self.entry_number_lesson.get(),
                         self.entry_name_lesson.get(),
                         begin_lesson,
                         end_lesson)

class Quit(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_quit()

    def init_quit(self):
        self.title('Quit')
        self.geometry("115x100+400+300")
        self.resizable(False, False)
        self.grab_set()
        self.focus_set()

        label_number_recess = ttk.Label(self, text='Are you sure?')
        label_number_recess.place(x=20, y=20)

        btn_add = tk.Button(self, text='Yes', command=self.master.destroy)
        btn_add.place(x=20, y=50)
        btn_close = tk.Button(self, text='No', command=self.destroy)
        btn_close.place(x=65, y=50)

class DB:
    def __init__(self):
        self.conn = sql.connect('lessons.db')
        self.c = self.conn.cursor()
        self.c.execute('''CREATE TABLE IF NOT EXISTS lessons_mon (number_lesson integer primary key, name_lesson text, begin_lesson text, end_lesson text)''')
        self.conn.commit()

    def insert_data(self, number_lesson, name_lesson, begin_lesson, end_lesson, day_db):
        self.c.execute('''INSERT INTO %s (number_lesson, name_lesson, begin_lesson, end_lesson) VALUES(?, ?, ?, ?)''' % day_db, (number_lesson, name_lesson, begin_lesson, end_lesson))
        self.conn.commit()



if __name__  ==  "__main__":
    root = tk.Tk()
    db = DB()
    app = Main(root)
    app.pack()
    root.title("Lessons")
    root.geometry("650x450+300+200")
    root.resizable(False, False)
    root.mainloop()