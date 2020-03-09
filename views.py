import os
from flask import jsonify, render_template, request, abort, redirect, current_app
import pandas as pd


def configure(app):

    @app.route('/', methods=['GET', 'POST'])
    def index():
        if request.method == 'GET':
            collection = current_app.db.video.find(sort={'theme_video': 1})
            return render_template(
                'index.html', title="List view", data=collection
            )
        else:
            theme_video = request.form.get('theme_video')
            name_video = request.form.get('name_video')
            f = request.files['file']
            if not theme_video or not f or not name_video:
                abort(400, "Invalid data")
            else:
                basepath = os.path.dirname(__file__)
                file = (name_video+'-'+str(f.filename)).replace(' ', '_')
                file_path = os.path.join(basepath, 'static/uploads', file)
                f.save(file_path)
                current_app.db.video.insert_one(
                    {
                        'theme_video': theme_video, 'name_video': name_video, 'file': file, 'like': 0, 'unlike': 0
                    }
                )
                return redirect("/new")

    @app.route('/new', methods=['GET'])
    def new():
        if request.method == 'GET':
            return render_template(
                'save.html', title="Success"
            )

    @app.route("/<string:tp>/<string:id>/<string:qtd>", methods=["GET"])
    def like(tp, id, qtd):
        current_app.db.video.update_one({"_id": id}, {"$set": {tp: qtd}})
        return "success"

    @app.route('/themes', methods=['GET', 'POST'])
    def themes():
        def myFunc(e):
            return e[3]
        if request.method == 'GET':
            themes = []
            list_themes = []
            collection = current_app.db.video.find(sort={'theme_video': 1})
            for theme in collection:
                if theme not in themes:
                    themes.append(theme['theme_video'])

            themes = sorted(set(themes))
            for theme_video in themes:
                collection = current_app.db.video.find(
                    {'theme_video': theme_video})
                likes = 0
                unlikes = 0
                for like in collection:
                    likes += int(like['like'])
                    unlikes += int(like['unlike'])

                p = likes-(unlikes/2)
                list_themes.append((theme_video, likes, unlikes, p))

            list_themes.sort(reverse=True, key=myFunc)

            return render_template(
                'themes.html',title="List",list_themes=list_themes
            )
