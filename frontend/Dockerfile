FROM nginx:alpine

WORKDIR /app
# Copy the built frontend from the previous stage to the NGINX web server
COPY . /usr/share/nginx/html

# Expose port 80 to the outside world
EXPOSE 80

# Start NGINX when the container starts
CMD ["nginx", "-g", "daemon off;"]