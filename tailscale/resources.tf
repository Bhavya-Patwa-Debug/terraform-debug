data "tailscale_acl" "remote_acl" {

}


resource "tailscale_acl" "as_json" {
  acl = jsonencode({
    acls : [
      {
        // Allow all users access to all ports.
        action : "accept",
        users : ["*"],
        ports : ["*:*"],
      },
    ],
  })
}

# resource "tailscale_acl" "as_hujson" {
#   acl = <<EOF
#   {
#     // Comments in HuJSON policy are preserved when the policy is applied.
#     "acls": [
#       {
#         // Allow all users access to all ports.
#         "action" : "accept",
#         "users"  : ["*"],
#         "ports"  : ["*:*"],
#       },
#     ],
#   }
#   EOF
# }

resource "tailscale_tailnet_key" "sample_key" {
  reusable      = true
  ephemeral     = false
  preauthorized = true
  expiry        = 3600
  description   = "Sample key"
}
