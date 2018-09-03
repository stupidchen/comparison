from flask import Blueprint, request, render_template, flash

bp = Blueprint('program', __name__)


class ProgramType:
    Python = 1
    Shell = 2


def run(program, type=ProgramType.Shell, round=1):
    return 1


@bp.route('/calculate', methods=('POST',))
def calculate():
    if request.method == 'POST':
        body = request.json
        ret = {}
        if isinstance(body, list):
            for data in body:
                ret[data['id']] = run(data['program'], data['type'], data['round'])

            return render_template('program.html', ret=ret)
        else:
            error = 'Invalid request body'
    else:
        error = 'Unsupported method'

    flash(error)


@bp.route('/test', methods=('GET',))
def test():
    ret = run('23')
    return render_template('program.html', ret=ret)
