import os
import faust

print('Inside app.py')


class Transaction(faust.Record):
    source: str
    target: str
    amount: float
    currency: str


print('Transaction class defined.')

app = faust.App('detector-app', broker=os.environ['KAFKA_BOOTSTRAP_SERVER'])
print('Faust app defined.')

transactions_topic = app.topic(
    os.environ['TRANSACTIONS_TOPIC'], value_type=Transaction)
print('Topic set.')


@app.task
async def detector_task():
    async for t in transactions_topic.stream():
        print(t.amount)

if __name__ == '__main__':
    print('Inside app.py __main__')
    app.main()
