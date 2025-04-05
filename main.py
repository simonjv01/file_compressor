import FreeSimpleGUI as sg

label1 = sg.Text("Select files to compress:")
input1 = sg.Input(size=(25, 1), key='-IN-')
choose_button = sg.FilesBrowse("Browse", key='-BROWSE-')

label2 = sg.Text("Select destination folder:")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose")

compress_button = sg.Button("Compress", key='-COMPRESS-')

window = sg.Window("File Compressor", 
                   layout=[[label1, input1, choose_button],
                           [label2, input2, choose_button2],
                           [compress_button]],)


window.read()
window.close()


