from flask import Flask,render_template,request
app = Flask(__name__)


@app.route('/fileread')
def content():

	try:
		params = request.args.to_dict()
		if 'file_name' in params:
			filename = params.get('file_name')
		else:
			filename='file1'
		filename = str(filename + '.txt')
		with open(filename, 'r',encoding='latin1') as f:

			if 'start' in params and 'end' in params:
				start = int(params.get('start'))
				end = int(params.get('end')) + 1
				file_content = f.readlines()[start:end]
				file_content = ''.join(file_content)

			else:
				file_content = f.read()

			return render_template('content.html', text=file_content)
	except Exception as e:
		return render_template('content.html', text=e)

if __name__ == '__main__':
    app.run()