FROM node:18-alpine

RUN apk add --no-cache git

WORKDIR /app

RUN git clone https://github.com/eMahtab/node-express-hello-world.git .

RUN npm install

EXPOSE 3000

CMD ["npm", "start"]