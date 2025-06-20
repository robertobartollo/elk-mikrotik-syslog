
# Instruções para coletar logs da Mikrotik RB750GR3 com ELK via Docker

## 1. Pré-requisitos
- Docker Desktop instalado
- Porta UDP 514 liberada no firewall
- Mikrotik com IP fixo da máquina Docker

## 2. Como rodar

Abra o terminal na pasta do projeto e execute:

```
docker-compose up -d
```

Acesse:
- Kibana: http://localhost:5601
- Elasticsearch: http://localhost:9200

## 3. Configurar Mikrotik

No Mikrotik, execute:

```
/system logging action add name=logstash target=remote remote=SEU_IP_DO_PC remote-port=514 remote-protocol=udp
/system logging add action=logstash topics=firewall
```

Substitua `SEU_IP_DO_PC` pelo IP do seu computador que está rodando o Docker.

## 4. Visualizar logs no Kibana

1. Acesse o Kibana
2. Vá em **Stack Management > Index Patterns**
3. Crie um padrão `mikrotik-logs-*`
4. Use `@timestamp` como campo de tempo
5. Vá em **Discover** para ver os logs

Pronto! Agora você pode monitorar os logs do firewall da Mikrotik RB750GR3 via Docker ELK.


## 5. Filtro GeoIP

O Logstash está configurado para aplicar GeoIP baseado no IP do roteador Mikrotik. 
Certifique-se de que o contêiner tenha acesso ao banco GeoLite2, que já está incluído na imagem do Logstash oficial.

## 6. Dashboard personalizado

O arquivo `kibana-dashboard.json` incluso pode ser importado em:
- Kibana > Stack Management > Saved Objects > Import



## 7. Dashboard avançado

Para importar todos os objetos visuais:

1. Acesse Kibana > Stack Management > Saved Objects
2. Clique em "Import" e importe:
   - kibana-dashboard.json
   - geoip-map.json
   - geoip-country-count.json

3. Depois vá para "Dashboard" e abra "Mikrotik GeoIP Dashboard"

