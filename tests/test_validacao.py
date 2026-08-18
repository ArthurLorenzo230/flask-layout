from app import app


def test_validacao_page_loads():
    client = app.test_client()
    response = client.get('/validacao')

    assert response.status_code == 200
    assert b'Nome' in response.data
    assert b'Sobrenome' in response.data
    assert b'Idade' in response.data


def test_validacao_page_returns_right_rules():
    client = app.test_client()
    response = client.post(
        '/validacao',
        data={'nome': 'Maria', 'sobrenome': 'Souza', 'idade': '18'}
    )

    assert response.status_code == 200
    assert b'Pode votar: Sim' in response.data
    assert b'Pode dirigir: Sim' in response.data


def test_layout_links_css_and_uses_site_header():
    client = app.test_client()
    response = client.get('/')

    assert response.status_code == 200
    assert b'/static/menu.css' in response.data
    assert b'class="site-header"' in response.data
    assert b'class="menu"' in response.data
