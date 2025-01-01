import shutil

def deploy_model(model_path, deployment_path):
    # Deploy the updated model by copying it to the deployment path
    shutil.copy(model_path, deployment_path)
    print(f"Model deployed to {deployment_path}")

if __name__ == "__main__":
    deploy_model("updated_model.h5", "/path/to/pwnagotchi/model_directory")
