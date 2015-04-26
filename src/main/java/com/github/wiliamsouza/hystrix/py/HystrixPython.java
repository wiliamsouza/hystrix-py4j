package com.github.wiliamsouza.hystrix.py;

import py4j.GatewayServer;
import com.netflix.hystrix.HystrixCommand;

public class HystrixPython {

  public static void main(String[] args) {
    HystrixPython py = new HystrixPython();
    GatewayServer server = new GatewayServer(py);
    server.start();
  }
}
