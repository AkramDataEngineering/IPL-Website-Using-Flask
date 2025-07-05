from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    teams = [
        {
            'name': 'Chennai Super Kings',
            'matches': 5,
            'won': 4,
            'lost': 1,
            'points': 8,
            'nrr': '+1.25',
            'captain': 'MS Dhoni',
            'logo': 'csk.jpeg'
        },
        {
            'name': 'Mumbai Indians',
            'matches': 5,
            'won': 3,
            'lost': 2,
            'points': 6,
            'nrr': '+0.85',
            'captain': 'Rohit Sharma',
            'logo': 'mi.jpeg'
        },
        {
            'name': 'Royal Challengers Bangalore',
            'matches': 5,
            'won': 2,
            'lost': 3,
            'points': 4,
            'nrr': '-0.50',
            'captain': 'Virat Kohli',
            'logo': 'rcb.jpeg'
        },
        {
            'name': 'Lucknow Super Giants',
            'matches': 5,
            'won': 3,
            'lost': 2,
            'points': 6,
            'nrr': '+0.70',
            'captain': 'KL Rahul',
            'logo': 'lsg.png'
        },
        {
            'name': 'Delhi Capitals',
            'matches': 5,
            'won': 2,
            'lost': 3,
            'points': 4,
            'nrr': '-0.40',
            'captain': 'Rishabh Pant',
            'logo': 'dc.png'
        },
        {
            'name': 'Kolkata Knight Riders',
            'matches': 5,
            'won': 3,
            'lost': 2,
            'points': 6,
            'nrr': '+0.65',
            'captain': 'Shreyas Iyer',
            'logo': 'kkr.jpg'
        },
        {
            'name': 'Sunrisers Hyderabad',
            'matches': 5,
            'won': 2,
            'lost': 3,
            'points': 4,
            'nrr': '-0.30',
            'captain': 'Pat Cummins',
            'logo': 'srh.jpg'
        }
    ]
    return render_template('ipl.html', teams=teams)

if __name__ == '__main__':
    app.run(debug=True)