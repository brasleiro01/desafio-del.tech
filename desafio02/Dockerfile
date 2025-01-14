# Use a imagem oficial do Nginx como base
FROM alpine:latest


RUN apk update && apk add --no-cache nginx
# Copie o arquivo HTML para o diretório de conteúdo do Nginx
COPY index.html /usr/share/nginx/html/

# Copie o arquivo de configuração customizado para o Nginx
COPY nginx.conf /etc/nginx/nginx.conf

# Exponha a porta 80
EXPOSE 80

# O Nginx irá iniciar automaticamente ao rodar o container
CMD ["nginx", "-g", "daemon off;"]