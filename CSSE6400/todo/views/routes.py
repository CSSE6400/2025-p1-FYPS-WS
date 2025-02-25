from flask import Blueprint, jsonify
api = Blueprint('api', __name__, url_prefix='/api/v1')

@api.route('/health')
def health():
    return jsonify({'status': 'ok'})

@api.route('/todos',methods=['GET'])
def get_todos():
    return jsonify([{
        'id': 1,
        'title': 'Watch CSSE6400 Lecture',
        'description': 'Watch CSSE6400 Lecture on ECHO360 for week 1',
        'completed': True,
        'deadline': '2025-02-05T00:00:00',
        'created_at': '2025-02-03T00:00:00',
        'updated_at': '2025-02-03T00:00:00',
    }])

@api.route('/todos/<int:id>', methods=['GET'])
def get_todo(id):
    return jsonify({
        'id': id,
        'title': 'Watch CSSE6400 Lecture',
        'description': 'Watch CSSE6400 Lecture on ECHO360 for week 1',
        'deadline': '2025-02-05T00:00:00',
        'created_at': '2025-02-03T00:00:00',
        'updated_at': '2025-02-03T00:00:00',
    })

@api.route('/todos',methods = ['POST'])
def create_todos():
    return jsonify({
        'id': 1,
        'title': 'Watch CSSE6400 Lecture',
        'description': 'Watch CSSE6400 Lecture on ECHO360 for week 1',
        'completed': True,
        'deadline': '2025-02-05T00:00:00',
        'created_at': '2025-02-03T00:00:00',
        'updated_at': '2025-02-03T00:00:00',
    }), 201
@api.route('/todos/<int:id>', methods=['PUT'])
def update_todo(id):
    return jsonify({
        'id': id,
        'title': 'Watch CSSE6400 Lecture',
        'description': 'Watch CSSE6400 Lecture on ECHO360 for week 1',
        'completed': True,
        'deadline': '2025-02-05T00:00:00',
        'created_at': '2025-02-03T00:00:00',
        'updated_at': '2025-02-03T00:00:00',
    })

@api.route('/todos/<int:id>', methods=['DELETE'])
def delete_todo(id):
    return jsonify({
        'id': id,
        'title': 'Watch CSSE6400 Lecture',
        'description': 'Watch CSSE6400 Lecture on ECHO360 for week 1',
        'completed': True,
        'deadline': '2025-02-05T00:00:00',
        'created_at': '2025-02-03T00:00:00',
        'updated_at': '2025-02-03T00:00:00',
    })