node {
  def appName = 'flask-hello'
  def imageTag = "registry.k8s.gent:30000/${appName}:master.${env.BUILD_NUMBER}"

  checkout scm

  stage 'Build image'
  sh("docker build -t ${imageTag} .")

  stage 'Push image to registry'
  withCredentials([[$class: 'UsernamePasswordMultiBinding', credentialsId: 'fb8c7f8b-2f8d-4769-bc4a-8b659c8dac5c',
    usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD']]) {
    sh('echo uname=$USERNAME pwd=$PASSWORD')
    sh('docker login -u$USERNAME -p$PASSWORD registry.k8s.gent:30000')
    sh("docker push ${imageTag}")
  }

  stage "Deploy Application"
  sh("sed -i.bak 's#IMAGE#${imageTag}#' flask-hello-k8s.yaml")
  sh("curl -O https://storage.googleapis.com/kubernetes-release/release/v1.6.6/bin/linux/amd64/kubectl")
  sh("chmod +x kubectl")
  sh("./kubectl apply -f flask-hello-k8s.yaml")
}
