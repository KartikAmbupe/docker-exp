# Use the official Node.js 16 image
FROM node:16-alpine

# Set the working directory
WORKDIR /usr/src/app

# Copy package files and install dependencies
COPY package*.json ./
RUN npm install

# Copy the application source code
COPY . .

# Expose port 3000
EXPOSE 3000

# The command to start the server
CMD ["npm", "start"]