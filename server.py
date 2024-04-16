from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
from flask import redirect, url_for

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
"2":{
    "lesson_id": 2,
    "country": "Indonesia",
    "title": "Top 3 famous Architectural Styles in Indonesia",
    "card_images": ["images/Batak_Toba_House.jpeg", "images/...", "images/..."],
    "card_text_title": ["Toba Batak Architecture", "...", "..."],
    "card_text": ["Toba Batak architecture reflects the architectural styles and practices specific to the Toba Batak community in North Sumatra, Indonesia.", "..", ".."],
    "texts": ["Toba Batak architecture encompasses the architectural styles and practices of the Toba Batak community in North Sumatra, Indonesia. Characterized by boat-shaped structures adorned with elaborately carved gables and gracefully sloping roof ridges, Toba Batak houses are a distinctive feature of this cultural tradition.", " ...", " ..."],
    "images": [["images/toba_1.png", "images/..."],["images/...", "images/..."], ["images/...", "images/..."]],
    "image_captions": [["Toba Batak house near Lake Toba, Indonesia", "..."], ["...", "..."], ["...", "..."]],
},
"3":{
    "lesson_id": 3,
    "country": "Malaysia",
    "title": "Top 3 famous Architectural Styles in Malaysia",
    "card_images": ["images/...", "images/...", "images/..."],
    "card_text_title": ["...", "...", "..."],
    "card_text": ["...", "..", ".."],
    "texts": ["....", " ...", " ..."],
    "images": [["images/...", "images/..."],["images/...", "images/..."], ["images/...", "images/..."]],
    "image_captions": [["...", "..."], ["...", "..."], ["...", "..."]],
},
"4":{
    "lesson_id": 4,
    "country": "Philippines",
    "title": "Top 3 famous Architectural Styles in Philippines",
    "card_images": ["images/...", "images/...", "images/..."],
    "card_text_title": ["...", "...", "..."],
    "card_text": ["...", "..", ".."],
    "texts": ["....", " ...", " ..."],
    "images": [["images/...", "images/..."],["images/...", "images/..."], ["images/...", "images/..."]],
    "image_captions": [["...", "..."], ["...", "..."], ["...", "..."]],
},
}

quiz = {
"1": {
"image": "images/quiz2.png",
"options": ["Indonesia", "Thailand", "Philippines", "Malaysia"],
"answer": "Indonesia",
"explanation": "This building has Toba Batak architecturual styles like a curved boat roof which is found in Indonesian architecture.",
},
"2": {
"image": "images/quiz1.png",
"options": ["Indonesia", "Thailand", "Philippines", "Malaysia"],
"answer": "Thailand",
"explanation": "This building has dragon roof finials, tiered roofs, and a tower with indented corners. These 3 architectural styles are found in Thai architecture.",
},
"3": {
"image": "images/quiz4.png",
"options": ["Indonesia", "Thailand", "Philippines", "Malaysia"],
"answer": "Philippines",
"explanation": "",
},
"4": {
"image": "images/quiz3.png",
"options": ["Indonesia", "Thailand", "Philippines", "Malaysia"],
"answer": "Malaysia",
"explanation": "",
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

quiz_answers = {}

@app.route('/quiz/<int:quiz_id>', methods=['GET', 'POST'])
def quiz_page(quiz_id):
    current_quiz = quiz.get(str(quiz_id))
    if not current_quiz:
        return "Quiz not found", 404

    if request.method == 'POST':
        selected_option = request.form['option']
        quiz_answers[str(quiz_id)] = selected_option

        if len(quiz_answers) == len(quiz):
            num_correct = sum(1 for quiz_id, answer in quiz_answers.items() if quiz[quiz_id]['answer'] == answer)
            total_questions = len(quiz)
            score = f"{num_correct}/{total_questions}"
            return render_template('quiz_results.html', score=score)
        else:
            next_quiz_id = quiz_id + 1
            if next_quiz_id <= len(quiz):
                return redirect(url_for('quiz_page', quiz_id=next_quiz_id))
            else:
                return redirect(url_for('quiz_results'))

    return render_template('quiz.html', quiz=current_quiz, quiz_id=quiz_id)

@app.route('/quiz_results')
def quiz_results():
    return render_template('quiz_results.html', quiz_answers=quiz_answers, quiz=quiz)

# AJAX FUNCTIONS

if __name__ == '__main__':
   app.run(debug = True, port = 5001)
