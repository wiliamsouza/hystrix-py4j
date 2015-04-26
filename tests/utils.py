from multiprocessing import Value, Lock


class MockedTime():

    def __init__(self):
        self._time = Value('f', 0)
        self._lock = Lock()

    def current_time_in_millis(self):
        with self._lock:
            return self._time.value

    def increment(self, millis):
        with self._lock:
            self._time.value += millis
        return self.current_time_in_millis()


def java_gateway():
    from py4j.java_gateway import java_import, JavaGateway
    gateway = JavaGateway(auto_convert=True)
    jvm = gateway.jvm
    java_import(jvm, 'com.netflix.hystrix.util.HystrixRollingNumber')
    java_import(jvm, 'com.netflix.hystrix.util.HystrixRollingNumberEvent')
    java_import(jvm, 'com.netflix.hystrix.HystrixCommandProperties')
    java_import(jvm, 'com.netflix.hystrix.HystrixCommandProperties.Setter')
    return gateway
