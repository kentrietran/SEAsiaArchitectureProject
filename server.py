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
    "card_images": ["images/Batak_Toba_House.jpeg", "images/Minangkabau.jpeg", "images/joglo.jpeg"],
    "card_text_title": ["Toba Batak Architecture", "Minangkabau Architecture", "Joglo roof"],
    "card_text": ["Toba Batak architecture reflects the architectural styles and practices specific to the Toba Batak community in North Sumatra, Indonesia.", "Minangkabau architecture in Indonesia is renowned for its distinctive curved roof design, resembling buffalo horns, symbolizing strength and prosperity.", "Joglo roof architecture in Indonesia is characterized by its iconic tiered, pyramid-like structure with a central dome."],
    "texts": ["Toba Batak architecture encompasses the architectural styles and practices of the Toba Batak community in North Sumatra, Indonesia. Characterized by boat-shaped structures adorned with elaborately carved gables and gracefully sloping roof ridges, Toba Batak houses are a distinctive feature of this cultural tradition.", "Minangkabau architecture in Indonesia is renowned for its distinctive curved roof design, resembling buffalo horns, symbolizing strength and prosperity. These traditional houses, called rumah gadang, are built on stilts and feature intricate wood carvings and vibrant colors. They reflect the matrilineal culture of the Minangkabau people and serve as communal spaces for social gatherings and ceremonies.", "Joglo roof architecture in Indonesia is characterized by its iconic tiered, pyramid-like structure with a central dome. These roofs, found in traditional Javanese houses known as joglos, are typically made of teak wood and intricately carved. Joglo roofs symbolize status and cultural heritage and are designed to provide natural ventilation and coolness."],
    "images": [["images/toba_1.png", "images/toba_2.png"],["images/m-1.png", "images/m-2.jpeg"], ["images/joglo_1.jpeg", "images/joglo_2.jpeg"]],
    "image_captions": [["Toba Batak house near Lake Toba, Indonesia", "Toba Batak Architecture"], ["Minangkabau Architecture", "Minangkabau Architecture"], ["Joglo roof", "Joglo roof"]],
},
"3":{
    "lesson_id": 3,
    "country": "Malaysia",
    "title": "Top 3 famous Architectural Styles in Malaysia",
    "card_images": ["images/pitched_roof.jpeg", "images/lh.jpeg", "images/peranakan.jpeg"],
    "card_text_title": ["Pitched Roofs", "Malaysian Longhouse", "Peranakan architecture"],
    "card_text": ["Pitched roof architecture in Malaysia typically features steeply sloped roofs with gable ends.", "Typically constructed from bamboo, wood, and thatch, these longhouses are designed to accommodate multiple families within separate living spaces called biliks, connected by a common veranda known as the ruai.", "Peranakan architecture reflects the unique cultural fusion of Chinese, Malay, and European influences, especially prominent during the colonial period."],
    "texts": ["Pitched roof architecture in Malaysia typically features steeply sloped roofs with gable ends. These roofs, often constructed using traditional materials like timber or thatch, are designed to withstand the tropical climate, heavy rainfall, and provide natural ventilation. They are commonly found in various traditional Malay houses and reflect the cultural and environmental influences on Malaysian architecture.", "The Malaysian longhouse is a traditional dwelling common among indigenous communities in Malaysia, such as the Iban, Bidayuh, and Orang Asli. It is a communal dwelling characterized by its elongated structure, built on stilts and often stretching for significant lengths. Typically constructed from bamboo, wood, and thatch, these longhouses are designed to accommodate multiple families within separate living spaces called biliks, connected by a common veranda known as the ruai. The longhouse serves as a central hub for social activities, ceremonies, and community gatherings, reflecting the close-knit and communal lifestyle of the indigenous peoples of Malaysia.", "Peranakan architecture reflects the unique cultural fusion of Chinese, Malay, and European influences, especially prominent during the colonial period. Peranakan houses in Malaysia often showcase distinctive features such as vibrant colors, intricate tile work, ornate carvings, and louvred windows, contributing to the rich architectural heritage of the country."],
    "images": [["images/pitchedroof1.jpeg", "images/pitchedroof2.jpeg"],["images/lh1.jpeg", "images/lh2.jpeg"], ["images/peranakan1.jpeg", "images/peranakan2.jpeg"]],
    "image_captions": [["Pitched Roofs", "Pitched Roofs"], ["Malaysian Longhouse", "Malaysian Longhouse"], ["Peranakan architecture", "Peranakan architecture"]],
},
"4":{
    "lesson_id": 4,
    "country": "Philippines",
    "title": "Top 3 famous Architectural Styles in Philippines",
    "card_images": ["images/nipahut.jpeg", "images/fortpilar.jpeg", "images/sh.jpeg"],
    "card_text_title": ["Nipa hut", "Spanish colonial fortifications", "Stone House"],
    "card_text": ["The  Nipa hut (bahay kubo) is a traditional stilt house found in the Philippines made of materials found in nature such as wood, bamboo and cogon grass.", "Spanish colonial fortifications served as defensive structures against foreign invaders and were often built using locally available materials such as stone and coral.", "Bahay na bato, literally translated as 'house of stone,' is a traditional architectural style in the Philippines that emerged during the Spanish colonial period."],
    "texts": ["The  Nipa hut (bahay kubo) is a traditional stilt house found in the Philippines, symbolizing Philippine culture. Originating in lowland areas under Spanish rule, its design influenced colonial-era bahay na bato architecture.", "Spanish colonial fortifications in the Philippines are characterized by robust architectural designs, featuring thick walls, strategically placed bastions, and imposing structures such as forts and watchtowers. These fortifications served as defensive structures against foreign invaders and were often built using locally available materials such as stone and coral.", "Bahay na bato, literally translated as 'house of stone,' is a traditional architectural style in the Philippines that emerged during the Spanish colonial period. It combines indigenous Filipino and Spanish influences, featuring sturdy stone lower floors and wooden upper floors. The lower level typically serves as storage or housing for livestock, while the upper level is the main living space. These houses often have large windows and spacious balconies, reflecting a blend of Spanish colonial and native Filipino design elements."],
    "images": [["images/nipahut1.jpeg", "images/nipahut2.jpeg"],["images/fortcuyo.jpeg", "images/fortsantiago.jpeg"], ["images/sh1.jpeg", "images/sh2.jpeg"]],
    "image_captions": [["Nipa hut", "Nipa hut"], ["Fort Cuyo", "Fort Santiago"], ["Stone House", "Stone House"]],
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
"image": "images/quiz4.jpeg",
"options": ["Indonesia", "Thailand", "Philippines", "Malaysia"],
"answer": "Philippines",
"explanation": "This building is made of stone and is one of the Spanish colonial fortifications found in the Philippines.",
},
"4": {
"image": "images/quiz3.jpeg",
"options": ["Indonesia", "Thailand", "Philippines", "Malaysia"],
"answer": "Malaysia",
"explanation": "This building is bright and colorful, displaying cultural fusion of Chinese, Malay, and European influences, which is commonly found in Malaysian Peranakan architecture.",
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
        next_quiz_id = quiz_id + 1

        if next_quiz_id > len(quiz):
            num_correct = sum(1 for qid, answer in quiz_answers.items() if quiz[qid]['answer'] == answer)
            total_questions = len(quiz)
            score = f"{num_correct}/{total_questions}"
            return render_template('quiz_results.html', score=score, quiz_answers=quiz_answers, quiz=quiz)
        else:
            return redirect(url_for('quiz_page', quiz_id=next_quiz_id))

    is_last_question = (quiz_id == len(quiz))
    return render_template('quiz.html', quiz=current_quiz, quiz_id=quiz_id, is_last_question=is_last_question)


@app.route('/quiz_results')
def quiz_results():
    return render_template('quiz_results.html', quiz_answers=quiz_answers, quiz=quiz)

# AJAX FUNCTIONS

if __name__ == '__main__':
   app.run(debug = True, port = 5001)
