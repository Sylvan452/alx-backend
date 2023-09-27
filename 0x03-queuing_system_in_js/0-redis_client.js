import { createClient } from 'redis';

function redisConnect() {
  const client = createClient();

  client.on('connect', function() {
    console.log('Redis client is connected to the server');
  }).on('error', (err) => {
    console.log(`Redis client is not connected to the server: ${err}`);
  });

};

redisConnect();