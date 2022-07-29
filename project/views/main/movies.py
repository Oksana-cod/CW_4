from flask import request
from flask_restx import Namespace, Resource

from project.container import movie_service
from project.setup.api.models import movie
from project.setup.api.parsers import pr_movie

api = Namespace('movies')


@api.route('/')
class MoviesView(Resource):
    @api.expect(pr_movie)
    @api.marshal_with(movie, as_list=True, code=200, description='OK')
    def get(self):
        """
        Get all movies.
        """

        status = request.args.get('status')

        return movie_service.get_all(filter=status,**pr_movie.parse_args())


@api.route('/<int:movie_id>/')
class MovieView(Resource):
    @api.response(404, 'Not Found')
    @api.marshal_with(movie, code=200, description='OK')
    def get(self, movie_id: int):
        """
        Get movie by id.
        """
        return movie_service.get_item(movie_id)