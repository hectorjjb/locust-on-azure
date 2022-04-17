from locust import FastHttpUser, task, constant

class QuickstartUser(FastHttpUser):
    wait_time = constant(0)

    def on_start(self):
        self.client.headers['User-Agent'] = "Mozilla/5.0"

    @task
    def index_page(self):
        self.client.get("/")