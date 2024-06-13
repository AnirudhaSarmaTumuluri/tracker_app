from flask import Flask, render_template, request, redirect, url_for
from db_scripts import *

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        workout = 'workout' in request.form
        leetcode = 'leetcode' in request.form
        cs_concepts = 'cs_concepts' in request.form
        journal = 'journal' in request.form
        moisturize = 'moisturize' in request.form
        minoxidil = 'minoxidil' in request.form
        thoughts = request.form.get('thoughts')
        print(request.form)

        # For demonstration purposes, we'll just print the values to the console
        print(f"Workout: {workout}")
        print(f"Leetcode: {leetcode}")
        print(f"CS Concepts Learning: {cs_concepts}")
        print(f"Journal: {journal}")
        print(f"Moisturize before bed: {moisturize}")
        print(f"Minoxidil: {minoxidil}")
        print(f"Thoughts: {thoughts}")

        # You can add code here to process the data as needed
        
        return redirect(url_for('home'))

    return render_template('index.html')

@app.route('/journal', methods=['GET', 'POST'])
def journal():
    if request.method == 'POST':
        # entry_id = request.form['entry_id']
        entry_type = request.form['entry_type']
        content = request.form['content']  # Use 'content' for consistency


        if entry_type=="quote":
            update_quote(content)
        # Print the submitted data
        print("Form Data:")
        print(f"  Entry Type: {entry_type}")
        print(f"  Content: {content}")
        # ...No database update is performed...

    return render_template("journal_update.html")

if __name__ == '__main__':
    app.run(debug=True)
