from flask import Flask, Response
import time

app = Flask(__name__)

@app.route("/data")
def stream_data():
  """Continuously generates data and returns it as an SSE stream."""
  def generate_data():
    counter = 0
    while True:
      yield f"data: {counter}\n\n"  # Data prefixed with "data:" and separated by empty lines
      counter += 1
      counter = counter % 5
      time.sleep(1)

  response = Response(generate_data(), mimetype="text/event-stream")
  response.headers.set('Cache-Control', 'no-cache')
  response.headers.set('Content-Type', 'text/event-stream')
  response.headers.set('Access-Control-Allow-Origin','*')
  return response


if __name__ == "__main__":
  app.run(port=8999)
