from flask import Flask, render_template, request, redirect, url_for

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

if __name__ == '__main__':
    app.run(debug=True)
