from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)

lessons = {
"1":{
    "lesson_id": 1,
    "country": "Thailand",
    "title": "Top 3 famous Architectural Styles in Thailand",
    "card_images": ["images/roof_finial.png", "images/roof_tiers.png", "images/indented_corners.png"],
    "card_text_title": ["Roof Finials", "Roof Tiers", "Indented Corners"],
    "card_text": ["Roof finials, also known as chofa, are intricate decorative elements commonly found in Thai architecture.", "Thai roof tiers are a defining feature of traditional Thai architecture. Characterized by their multi-tiered design, these roofs typically consist of several layers, each adorned with intricate details and decorative elements.", "Inspired by traditional Thai design principles, structures often feature intricately carved wooden details, sloping roofs, and ornate decorations. The signature element of indented corners adds both aesthetic appeal and functionality, allowing buildings to better withstand heavy rains and strong winds common in the region."],
    "texts": ["These ornate structures adorn the apex of temple roofs and palace buildings, adding a touch of elegance and cultural significance to the skyline. Crafted with meticulous detail, roof finials often depict mythical creatures such as dragons or nāgas (half-human and half-serpent), symbolizing protection and prosperity in Thai culture. Their presence not only enhances the aesthetic appeal of the architecture but also serves as a reminder of Thailand's rich history and spiritual heritage.", "The tiered roof style serves both practical and symbolic purposes, providing ventilation and protection from the elements while also symbolizing prosperity and spiritual significance. This architectural tradition can be observed in various structures across Thailand, including temples, palaces, and traditional Thai houses, showcasing the country's rich cultural heritage and artistic craftsmanship.", "Indented corners represent a characteristic aspect of traditional Thai architecture, where the corners of a rectangular building are divided into multiple recessed sections."],
    "images": [["images/dragon_roof.png", "images/nagas_roof.png"],["images/roof_tiers1.png", "images/roof_tiers2.png"], ["images/indented_c_1.png", "images/indented_c_2.jpeg"]],
    "image_captions": [["Dragon roof finial", "Nagas roof finial"], ["The Sanctuary Of Truth building with roof tiers", "Temple Wat Chiang Man with roof tiers"], ["Temple of the Emerald Buddha with Indented Corners", "The Grand Place Temple with Indented Corners"]],
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
"3": {
"image": "images/dragon_roof.png",
"answer": "",
"page": "",
},
"4": {
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

@app.route('/lesson/<int:lesson_id>/<int:index>')
def lesson_detail(lesson_id, index):
    lesson = lessons.get(str(lesson_id))
    if lesson:
        return render_template('lesson.html', lesson=lesson, index=index)
    else:
        return "Lesson not found", 404

@app.route('/quiz')
def quiz():
   return render_template('quiz.html')

# AJAX FUNCTIONS

if __name__ == '__main__':
   app.run(debug = True, port = 5001)
