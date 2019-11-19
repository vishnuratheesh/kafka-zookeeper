# Kafka Broker + Zookeper Example

This is an example implementation of Kafka + Zookeeper based on a tutorial seen here: https://blog.florimond.dev/building-a-streaming-fraud-detection-system-with-kafka-and-python


- Broker

  ```docker-compose -f docker-compose.kafka.yml up```

- Fraud Detection App

  ```docker-compose -f docker-compose.yml up```



To track the Legit transactions topic:

```
docker-compose -f docker-compose.kafka.yml exec broker kafka-console-consumer --bootstrap-server localhost:9092 --topic streaming.transactions.legit
```


To track the Fraud transactions topic:

```
docker-compose -f docker-compose.kafka.yml exec broker kafka-console-consumer --bootstrap-server localhost:9092 --topic streaming.transactions.fraud
```


Additional Learnings:

- Zoo Navigator

  Helps to visualize/inspect zookeper.

- KaDeck (https://www.kadeck.com/)

  Helps visualize Kafka Topics and messages, useful for debugging.
  
  To get KaDeck to connect, had to add / modify these env settings on the kafka compose yml:
    
    ```
    KAFKA_LISTENER_SECURITY_PROTOCOL_MAP: PLAINTEXT:PLAINTEXT,PLAINTEXT_HOST:PLAINTEXT
    KAFKA_ADVERTISED_LISTENERS: PLAINTEXT://broker:9092,PLAINTEXT_HOST://localhost:29092
    ```
  
  And bind port `29092` to localhost. Then use KaDeck to connect.
  
