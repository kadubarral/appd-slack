from appd.request import AppDynamicsClient

c = AppDynamicsClient('https://sulamerica.saas.appdynamics.com', 'api', 'api', 'sulamerica')

def get_app():
    #return c.get_applications()
    app_list = []
    for app in c.get_applications():
        app_list.append(app.name)
    return app_list

if __name__ == "__main__":
    print(', '.join(get_app()))
    #print(get_app())