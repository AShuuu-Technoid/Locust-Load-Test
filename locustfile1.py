from locust import HttpUser, between, task


class WebsiteUser(HttpUser):
    wait_time = between(5, 15)

    def on_start(self):
        r = self.client.get("/")
        assert r.status_code == 200, "Unexpected response code: " + r.status_code
        # with self.client.post("/", catch_response=True) as response:
        #     if response.text != "Success":
        #         response.failure("Got wrong response")
        #     elif response.elapsed.total_seconds() > 0.5:
        #         response.failure("Request took too long")


    @task
    def index(self):
        with self.client.get("/", catch_response=True) as response:
            if response.text != "Success":
                response.failure("Failed")
            elif response.elapsed.total_seconds() > 0.5:
                response.failure("Request took too long")


    # @task
    # def about(self):
    #     self.client.get("/about/")
