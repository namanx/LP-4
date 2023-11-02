from PIL import Image
def extract_exif_data(image_path):
    with Image.open(image_path) as img:
        exif_data = img._getexif()
        if exif_data is not None:
            print("EXIF Data:")
            print(exif_data)
            for tag_id, value in exif_data.items():
                print(f"Tag ID: {tag_id}, Value: {value}")
            import tkinter as tk

            # Sample data
            data = exif_data

            # Create the main window
            root = tk.Tk()
            root.title("Image Information")
            root.geometry("650x250")
            # Create a Text widget to display the data
            text_widget = tk.Text(root, wrap=tk.NONE)
            text_widget.pack(fill="both", expand=True)
            
            # for item in exif_data:
            #     text_widget.insert(tk.END, f"Tag ID: {item}, Value: {exif_data[item]}\n")
            text_widget.insert(tk.END, f"Pointer of the Image is : {exif_data[34665]}\n")
            text_widget.insert(tk.END, f"Shutter Speed of the Image is : {exif_data[33434]}\n")
            text_widget.insert(tk.END, f"The Camera Brand Used for : {exif_data[271]}\n")
            text_widget.insert(tk.END, f"Date of Capture : {exif_data[36867]}\n")
         

            # Create a scrollbar for the Text widget
            scrollbar = tk.Scrollbar(text_widget)
            scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
            text_widget.config(yscrollcommand=scrollbar.set)
            scrollbar.config(command=text_widget.yview)

            # Start the tkinter main loop
            root.mainloop()
            
        else:
            print("No EXIF data found.")