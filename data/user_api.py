import flask
from data import db_session
from data.news import News
from data.users import User
from flask import jsonify, request 
blueprint = flask.Blueprint(
    'news_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/user')
def get_news():
    db_sess = db_session.create_session()
    user = db_sess.query(User).all()
    return jsonify(
        {
            'users':
                [item.to_dict(only=('name', 'about', 'email')) 
                 for item in user]
        }
    )

@blueprint.route('/api/user/<int:id>', methods=['GET'])
def get_one_news(id):
    db_sess = db_session.create_session()
    user = db_sess.query(User).get(id)
    if not user:
        return jsonify({'error': 'Not found'})
    return jsonify(
        {
            'user': user.to_dict(only=(
                'name', 'about', 'email'))
        }
    )

@blueprint.route('/api/user', methods=['POST'])
def create_user():
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ['name', 'about', 'email']):
        return jsonify({'error': 'Bad request'})
    db_sess = db_session.create_session()
    user = User(
        name=request.json['name'],
        about=request.json['about'],
        email=request.json['email'],
    )
    db_sess.add(user)
    db_sess.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/user/<id>', methods=['PUT'])
def change_user(id):
    if not request.json:
        return jsonify({'error': 'Empty request'})
    db_sess = db_session.create_session()
    user = db_sess.query(User).get(id)
    name = request.json["name"]
    email = request.json["email"]
    about = request.json["about"]
    user.name = name
    user.email = email
    user.about = about
    db_sess.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/user/<int:id>', methods=['DELETE'])
def delete_user(id):
    db_sess = db_session.create_session()
    user = db_sess.query(User).get(id)
    if not user:
        return jsonify({'error': 'Not found'})
    db_sess.delete(user)
    db_sess.commit()
    return jsonify({'success': 'OK'})