node {
  def appName = 'flask-hello'
  def imageTag = "registry.k8s.gent:30000/${appName}:${env.BRANCH_NAME}.${env.BUILD_NUMBER}"

  checkout scm

  stage 'Build image'
  sh("docker build -t ${imageTag} .")

  stage 'Push image to registry'
  // sh("docker push ${imageTag}")

  stage "Deploy Application"
  sh("sed -i.bak 's#IMAGE#${imageTag}#' flask-hello-k8s.yaml")
  sh("kubectl apply -f flask-hello-k8s.yaml")
}
