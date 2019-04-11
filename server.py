import json
import os
from src import image_comparer
from aiohttp import web


# =============================================================================
# Helpers

def get_utf8_json_response(value):
    res = web.Response(body=json.dumps(value, ensure_ascii=False).encode('utf-8'))
    res.content_type = 'application/json;charset=utf-8'
    return res


# =============================================================================
# Handlers

async def handle_compare(request):
    value = await request.json()
    method = value["method"]
    image_url1 = value["imageUrl1"]
    image_url2 = value["imageUrl2"]
    try:
        return get_utf8_json_response({
            'method': method,
            'score': image_comparer.compare(method, image_url1, image_url2)
        })
    except Exception as e:
        return get_utf8_json_response({"error": str(e)})


async def handle_health(request):
    return get_utf8_json_response({
        'message': 'up',
        'commit': os.environ.get('GIT_COMMIT'),
        'branch': os.environ.get('ENV')

    })


# =============================================================================
# Routes

app = web.Application()
app.add_routes([
    web.post('/compare', handle_compare),
    web.get('/health', handle_health)
])


# =============================================================================
# Main

def run_simple():
    # without gunicorn
    web.run_app(app, port=os.environ.get('SERVICE_PORT', 8080))


if __name__ == "__main__":
    run_simple()
