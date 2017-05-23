from appJar import gui

data=[["Контакт", "Телефон", "Электронный адрес", "Заметки"],
     ["Иван Абрамов", "8-955-123-45-67", "asdasd@asdasd.sad", "-"],
     ["Тина Хетагурова", "8-911-123-22-33", "asdsafjnif@asdasd.asd", "-"],
     ["Илья Ершин", "8-900-111-34-56", "dsfsdfn@dasd.sad", "-"]]
app=gui("Адресная книга")
app.setGeometry("700x" + str(max(70 + 25 * len(data), 200)))

def press(cellNum):
    global data
    if cellNum == "newRow":
        # new_name = app.textBox("Новый контакт", "Введите имя контакта")
        # new_phone = app.textBox("Новый контакт", "Введите номер телефона")
        # new_email = app.textBox("Новый контакт", "Введите электронный адрес")
        # new_note = app.textBox("Новый контакт", "Введите заметку")
        row=app.getGridEntries("g1")
        data.append(row)
        app.addGridRow("g1", row)
        # app.n_grids["g1"].addRows(data)
        print(len(app.n_grids["g1"].rows))
    else:
        row = app.n_grids["g1"].rows[cellNum]
        all_selected=app.getGridSelectedCells("g1")
        selected=[]
        selected_cell=None
        # check for selected cells
        print(all_selected)
        for i in range(4):
            print(str(cellNum) + "-" + str(i))
            if all_selected[str(cellNum-1) + "-" + str(i)]:
                selected.append(i)
        # for cell, status in app.getGridSelectedCells("g1").items():
        #     # if
        #     pass

        if selected == [] or 0 in selected:
            name = app.textBox("Изменение", "Введите имя контакта", row[0])
            # if name == None:
            #     data.remove(row)
            #     app.n_grids["g1"].addRows(data)
            #
            #     print(len(app.n_grids["g1"].rows))
            #     return
            # else:
            row[0] = name

        if selected == [] or 1 in selected:
            row[1] = app.textBox("Изменение", "Введите номер телефона", row[1])

        if selected == [] or 2 in selected:
            row[2] = app.textBox("Изменение", "Введите электронный адрес", row[2])

        if selected == [] or 3 in selected:
            row[3] = app.textBox("Изменение", "Введите заметку", row[3])

        data[cellNum] = row
        app.n_grids["g1"].addRows(data)

app.addGrid("g1", data, addRow=True, action=press, actionColumnText="Действие", actionButtonLabel="Изменить")

app.go()