import requests
from flask import Flask, jsonify

def get_all_gists(username):
    gists = []
    url = f"https://api.github.com/users/{username}/gists"

    try:
        while url:
            response = requests.get(url)
            response.raise_for_status()

            current_gists = response.json()
            gists.extend(current_gists)

            # Check for a Link header to determine if there are more pages
            links = response.headers.get('Link')
            if links:
                next_link = [link for link in links.split(',') if 'rel="next"' in link]
                if next_link:
                    url = next_link[0].split(';')[0][1:-1]
                else:
                    url = None
            else:
                url = None

        return gists
    except requests.exceptions.RequestException as e:
        print("In exception in get all gists")
        print(f"Error: {e}")
        return None


app = Flask(__name__)

@app.route('/<username>', methods=['GET'])
def get_gists_api(username):
    # print("in gist api", file=sys.stderr)
    gists = get_all_gists(username)

    if gists is None:
        return jsonify({"error": "Unable to retrieve gists"}), 500

    return jsonify({"gists": gists})

@app.errorhandler(Exception)
def handle_exception(err):
  path = request.path #

if __name__ == "__main__":
    # the default port 5000 seems to be not freeable in MacOS Sonoma.
    # Turning off airdrop/airplay and rebooting did not work for me
    # Leaving debug on as output is prettyprint vs without debug.
    app.run(debug=True, host='0.0.0.0', port=8080)

