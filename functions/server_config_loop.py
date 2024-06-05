servers=("server1" "server2" "server3")
for server in "${servers[@]}":
    configure_monitoring_agent "$server"
done


environments=("dev" "staging" "prod")
for env in "${environments[@]}":
    deploy_configuration "$env"
done

databases=("db1" "db2" "db3")
for db in "${databases[@]}":
     create_backup "$db"
done