from kubernetes import client, config

def create_deployment():
    # Load the Kubernetes configuration from default location or kubeconfig file
    config.load_kube_config(config_file='/app/config')

    # Create an instance of the Kubernetes API client
    api_instance = client.AppsV1Api()

    # Define the metadata for the Deployment
    metadata = client.V1ObjectMeta(name="vaccinedb-deployment")

    # Define the selector for the Deployment
    selector = client.V1LabelSelector(match_labels={"app": "vaccinedb"})

    # Define the labels for the Deployment's template
    labels = {"app": "vaccinedb"}

    # Define the container spec for the Deployment
    container = client.V1Container(
        name="sickleavedb-container",
        image="hub.leandevclan.com/vaccinedb:latest",
        ports=[client.V1ContainerPort(container_port=5000)]
    )

    # Define the template spec for the Deployment
    template = client.V1PodTemplateSpec(
        metadata=client.V1ObjectMeta(labels=labels),
        spec=client.V1PodSpec(containers=[container])
    )

    # Define the spec for the Deployment
    spec = client.V1DeploymentSpec(
        replicas=1,
        selector=selector,
        template=template
    )

    # Create the Deployment object
    deployment = client.V1Deployment(
        api_version="apps/v1",
        kind="Deployment",
        metadata=metadata,
        spec=spec
    )

    # Create the Deployment on the cluster
    api_instance.create_namespaced_deployment(
        namespace="test",
        body=deployment
    )

    print("vaccinedb Deployment created successfully.")



if __name__ == "__main__":
    create_deployment()
