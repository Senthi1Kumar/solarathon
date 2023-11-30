import solara
import requests

OURA_API_KEY = solara.reactive("")


def welcome_user(api_key:str):
    p_info_url = 'https://api.ouraring.com/v2/usercollection/personal_info'
    headers = {
        'Authorization': 'Bearer %s' % api_key
    }
    user_info = requests.request('GET', p_info_url, headers=headers)
    if user_info.status_code == 200:
        info = user_info.json()
        return f"Welcome {info['email'].split('@')[0]}"
    elif user_info.status_code == 400:
        return f'{user_info.status_code}: Client Exception'
    elif user_info.status_code == 401:
        return f'{user_info.status_code}: Unauthorized access exception. Usually means the access token is expired, malformed or revoked.'
    elif user_info.status_code == 403:
        return f'{user_info.status_code}: Access Forbidden'
    elif user_info.status_code == 429:
        return f'{user_info.status_code}: Request Rate Limit Exceeded.'
    

route_order = ["/", "heartrate"]

@solara.component
def Page():
    with solara.Column(style={"padding": "20px"}):
        solara.Title("Sleep Health App")
        solara.Markdown(r'''
        # Your sleep companion 💤
        
        The **Sleep Health** app is designed to improve sleep health and overall well-being by providing users with personalized insights and recommendations.
        Its purpose is to track and analyze sleep data using the [**OURA Ring**](https://ouraring.com/) API, a wearable device that captures sleep-related metrics such as sleep duration, sleep stages, and sleep quality.
        
        The target audience for the app includes individuals who are interested in optimizing their sleep and want to gain a better understanding of their sleep patterns.
        This may include people experiencing sleep-related issues, athletes looking to improve their recovery, or anyone who wants to prioritize their sleep for better health and performance.
    ''')
    
        with solara.Card("OURA Ring API key", margin=5):
            solara.Markdown("""If you have an Oura account, please get your API key and enter here!""")
            solara.InputText(label="API key", password= True, value=OURA_API_KEY)
            solara.Button(label="Save", on_click=lambda: welcome_user(OURA_API_KEY), outlined=True)

@solara.component
def Layout(children):
    # this is the default layout, but you can override it here, for instance some extra padding
    return solara.AppLayout(children=children, style={"padding": "20px"}, color="#4D77FF")
