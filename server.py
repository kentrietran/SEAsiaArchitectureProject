from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)

lessons = {
"1":{
    "lesson_id": 1,
    "title": "Top 3 famous Architectural Styles in Thailand",
    "card_image": "images/dragon_roof.png",
    "card_text_title": ["Roof Finials", "Roof Tiers", "Indented Corners"],
    "card_text": ["Roof finials, also known as chofa, are intricate decorative elements commonly found in Thai architecture.", "...", ".."],
    "texts": ["These ornate structures adorn the apex of temple roofs and palace buildings, adding a touch of elegance and cultural significance to the skyline. Crafted with meticulous detail, roof finials often depict mythical creatures such as dragons or nāgas (half-human and half-serpent), symbolizing protection and prosperity in Thai culture. Their presence not only enhances the aesthetic appeal of the architecture but also serves as a reminder of Thailand's rich history and spiritual heritage.", "...", "..."],
    "images": ["images/dragon_roof.png", "images/nagas_roof.png"],
    "image_captions": ["Dragon roof finial", "Nagas roof finial"],
},
"2":{
    "lesson_id": 2,
    "title": "Top 3 famous Architectural Styles in Indonesia",
    "card_image": "images/dragon_roof.png",
    "card_text_title": ["Roof Finials", "Roof Tiers", "Indented Corners"],
    "card_text": ["Roof finials, also known as chofa, are intricate decorative elements commonly found in Thai architecture.", "...", ".."],
    "texts": ["These ornate structures adorn the apex of temple roofs and palace buildings, adding a touch of elegance and cultural significance to the skyline. Crafted with meticulous detail, roof finials often depict mythical creatures such as dragons or nāgas (half-human and half-serpent), symbolizing protection and prosperity in Thai culture. Their presence not only enhances the aesthetic appeal of the architecture but also serves as a reminder of Thailand's rich history and spiritual heritage.", "...", "..."],
    "images": ["images/dragon_roof.png", "images/nagas_roof.png"],
    "image_captions": ["Dragon roof finial", "Nagas roof finial"],
},
"3":{
    "lesson_id": 3,
    "title": "Top 3 famous Architectural Styles in Malaysia",
    "card_image": "images/dragon_roof.png",
    "card_text_title": ["Roof Finials", "Roof Tiers", "Indented Corners"],
    "card_text": ["Roof finials, also known as chofa, are intricate decorative elements commonly found in Thai architecture.", "...", ".."],
    "texts": ["These ornate structures adorn the apex of temple roofs and palace buildings, adding a touch of elegance and cultural significance to the skyline. Crafted with meticulous detail, roof finials often depict mythical creatures such as dragons or nāgas (half-human and half-serpent), symbolizing protection and prosperity in Thai culture. Their presence not only enhances the aesthetic appeal of the architecture but also serves as a reminder of Thailand's rich history and spiritual heritage.", "...", "..."],
    "images": ["images/dragon_roof.png", "images/nagas_roof.png"],
    "image_captions": ["Dragon roof finial", "Nagas roof finial"],
},
"4":{
    "lesson_id": 4,
    "title": "Top 3 famous Architectural Styles in Philippines",
    "card_image": "images/dragon_roof.png",
    "card_text_title": ["Roof Finials", "Roof Tiers", "Indented Corners"],
    "card_text": ["Roof finials, also known as chofa, are intricate decorative elements commonly found in Thai architecture.", "...", ".."],
    "texts": ["These ornate structures adorn the apex of temple roofs and palace buildings, adding a touch of elegance and cultural significance to the skyline. Crafted with meticulous detail, roof finials often depict mythical creatures such as dragons or nāgas (half-human and half-serpent), symbolizing protection and prosperity in Thai culture. Their presence not only enhances the aesthetic appeal of the architecture but also serves as a reminder of Thailand's rich history and spiritual heritage.", "...", "..."],
    "images": ["images/dragon_roof.png", "images/nagas_roof.png"],
    "image_captions": ["Dragon roof finial", "Nagas roof finial"],
},
}

quiz = {
"1": {
"image": "images/dragon_roof.png",
"answer": "",
"page": "",
},
"2": {
"image": "images/dragon_roof.png",
"answer": "",
"page": "",
},
}

# ROUTES

@app.route('/')
def home():
   return render_template('home.html')

@app.route('/home2')
def home2():
   return render_template('home2.html')

@app.route('/learn/<lesson_id>')
def learn(lesson_id):
    lesson = lessons.get(lesson_id)
    if lesson:
        return render_template('learn.html', lesson=lesson)
    else:
        return "Lesson not found", 404

@app.route('/quiz')
def quiz():
   return render_template('quiz.html')

# AJAX FUNCTIONS

if __name__ == '__main__':
   app.run(debug = True, port = 5001)
